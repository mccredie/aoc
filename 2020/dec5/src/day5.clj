(ns day5)

(declare seat-id find-loner read-input)

(defn ex1 [opts]
  (println (reduce max (map seat-id (read-input)))))

(defn ex2 [opts]
  (println (find-loner (set (map seat-id (read-input))))))


(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

(defn row-part [boarding-pass]
  (subs boarding-pass 0 7))

(defn to-binary [zero-val one-val value]
  (reduce
    (fn [a b] (+ (* 2 a) b))
    0
    (map {zero-val 0 one-val 1} value)))

(defn row-value [row-part]
  (to-binary \F \B row-part))

(defn col-part [boarding-pass]
  (subs boarding-pass 7 10))

(defn col-value [col-part]
  (to-binary \L \R col-part))

(defn col-id [boarding-pass]
    (->>
      boarding-pass
      (col-part)
      (col-value)))

(defn row-id [boarding-pass]
    (->>
      boarding-pass
      (row-part)
      (row-value)))

(defn seat-id [boarding-pass]
  (+
    (* 8 (row-id boarding-pass))
    (col-id  boarding-pass)))


(defn empty-seats [seats]
  (reduce disj (set (range 1024)) seats))

(defn find-loner [seats]
  (->>
    (empty-seats seats)
    (filter (fn [seat] (and
                         (contains? seats (inc seat))
                         (contains? seats (dec seat)))))
    (first)))
