import sys
from dataclasses import dataclass


def main():
    data = read_input(sys.stdin)
    reader = PacketReader(data)

    packet, _ = reader.read_packet()

    print(process(packet))

def read_input(lines):
    out = []
    for line in lines:
        out.append("".join(NIBBLE2BIN[n] for n in line.strip()))
    return "".join(out)

NIBBLE2BIN = {
        hex(x)[2:].upper(): bin(x)[2:].rjust(4, '0')
        for x in range(16)
}


def process(packet):
    if packet.type_id == SUM:
        value = sum(process(p) for p in packet.packets)
    elif packet.type_id == PRODUCT:
        value = 1
        for p in packet.packets:
            value *= process(p)
    elif packet.type_id == MINIMUM:
        value = min(process(p) for p in packet.packets)
    elif packet.type_id == MAXIMUM:
        value = max(process(p) for p in packet.packets)
    elif packet.type_id == LITERAL:
        value = packet.value
    elif packet.type_id == GT:
        value = process(packet.packets[0]) > process(packet.packets[1])
    elif packet.type_id == LT:
        value = process(packet.packets[0]) < process(packet.packets[1])
    elif packet.type_id == EQ:
        value = process(packet.packets[0]) == process(packet.packets[1])
    return int(value)

def flatten_packets(packets):
    for packet in packets:
        yield packet
        if packet.type_id != LITERAL:
            yield from flatten_packets(packet.packets)


@dataclass
class Packet:
    version: int = None
    type_id: int = None

@dataclass
class LiteralPacket(Packet):
    value: int = None


@dataclass
class OperatorPacket(Packet):
    length_type_id: int = None
    total_length: int = None
    packets: list[Packet] = None

LITERAL = 4
SUM =  0
PRODUCT = 1
MINIMUM = 2
MAXIMUM = 3
GT = 5
LT = 6
EQ = 7

class PacketReader:
    def __init__(self, data):
        self.data = data
        self.offset = 0

    def read_packet(self):
        start = self.offset
        version = self.read_version()
        type_id = self.read_type_id()
        if type_id == LITERAL:
            packet = LiteralPacket()
            packet.version = version
            packet.type_id = type_id
            packet.value = self.read_literal()
        else:
            packet = OperatorPacket()
            packet.version = version
            packet.type_id = type_id
            packet.length_type_id = self.read_length_type_id()
            packet.packets = []
            if packet.length_type_id == 0:
                bits_read = 0
                packet.total_length = self.read_total_length(15)
                while bits_read < packet.total_length:
                    p, read = self.read_packet()
                    bits_read += read
                    packet.packets.append(p)

            else:
                packet.total_length = self.read_total_length(11)
                for _ in range(packet.total_length):
                    packet.packets.append(self.read_packet()[0])
        return packet, self.offset - start

    def read_version(self):
        return self._read_bits(3)

    def read_type_id(self):
        return self._read_bits(3)

    def read_literal(self):
        value = 0
        while True:
            value *= 16
            g = self._read_bits(1)
            value += self._read_bits(4)
            if g == 0:
                break
        return value

    def read_length_type_id(self):
        return self._read_bits(1)

    def read_total_length(self, bits):
        return self._read_bits(bits)

    def _read_bits(self, bits):
        value = int(self.data[self.offset:self.offset+bits], 2)
        self.offset += bits
        return value


if __name__ == "__main__":
    main()
