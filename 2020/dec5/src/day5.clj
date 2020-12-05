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

(defn row-value [row-part]
  (reduce
    (fn [a b] (+ (* 2 a) b))
    0
    (map (fn [c] (if (= c \F) 0 1)) row-part)))

(defn col-part [boarding-pass]
  (subs boarding-pass 7 10))

(defn col-value [col-part]
  (reduce
    (fn [a b] (+ (* 2 a) b))
    0
    (map (fn [c] (if (= c \L) 0 1)) col-part)))

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
  (reduce disj (set (range 1023)) seats))

(defn find-loner [seats]
  (->>
    (empty-seats seats)
    (filter (fn [seat] (and
                         (contains? seats (inc seat))
                         (contains? seats (dec seat)))))
    (first)))





