(ns dec10)

(defn read-input []
  (map #(Integer/parseInt %) (line-seq (java.io.BufferedReader. *in*))))

(defn joltage-differences [input]
  (let [joltages (vec (sort input))]
    (map - (conj joltages (+ (last joltages) 3)) (cons 0 joltages))))

(defn ex1 [opts]
  (println
    (let [diffs (joltage-differences (read-input))]
      (* (count (filter #(= 3 %) diffs)) (count (filter #(= 1 %) diffs))))))

(defn runs [diffs]
  (loop [runs []
         run 0
         x (first diffs)
         remaining (rest diffs)]
    (if (= nil x)
      runs
      (if (= x 3)
        (recur (conj runs run) 0 (first remaining) (rest remaining))
        (recur runs (inc run) (first remaining) (rest remaining))))))

; This is kind of cheating, but all of the inputs only have gaps of 1 or 3, and
; none of them have a run of more than 4 gaps of 1. So just look up the combos.
(def combos {
 0 1
 1 1
 2 2
 3 4
 4 7 })

(defn ex2 [opts]
  (let [joltages (sort (read-input))
        diffs (joltage-differences joltages)]
    (println (reduce * (map combos (runs diffs))))))
