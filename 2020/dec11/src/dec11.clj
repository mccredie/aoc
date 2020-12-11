(ns dec11
  (:require [clojure.set :as cset :refer [intersection, union]]))

(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

(defn parse-seats [lines]
  (reduce cset/union
    (for [[row  line] (map vector (range) lines)]
      (set
        (for [[col seat] (map vector (range) line) :when (= seat \L)]
          [col row])))))

(defn adjacent [[col row]]
  #{
    [ (dec col) (dec row) ]
    [ col (dec row) ]
    [ (inc col) (dec row) ]
    [ (dec col) row ]
    [ (inc col) row ]
    [ (dec col) (inc row) ]
    [ col (inc row) ]
    [ (inc col) (inc row) ]})

(defn will-be-occupied? [seat occupied]
  (let [is-occupied (occupied seat)
        adjacent-count (count (cset/intersection occupied (adjacent seat)))]
    (if (and (not is-occupied ) (zero? adjacent-count))
      true
      (if (and is-occupied (<= 4 adjacent-count))
        false
        is-occupied))))

(defn step [seats occupied]
  (set (filter #(will-be-occupied? % occupied) seats)))

(defn run-til-stable [seats]
  (loop [occupied #{}]
    (let [to-be-occupied (step seats occupied)]
      (if (= occupied to-be-occupied)
        occupied
        (recur to-be-occupied)))))

(defn ex1 [opts]
  (println (count (run-til-stable (parse-seats (read-input))))))

(defn lines-of-sight [[cols rows] seats]
  [
    ;up
    (fn [[col row]]
      (for [x (range (dec row) -1 -1)
            :when (seats [col x])]
        [col x]))
    ;diag up right
    (fn [[col row]]
      (for [n (next (range))
            :let [x (+ col n) y (- row n)]
            :while (and (< x cols)  (>= y 0))
            :when (seats [x y])]
        [x y]))
    ;right
    (fn [[col row]]
      (for [x (range (inc col) cols)
            :when (seats [x row])]
        [x row]))
    ;diag down right
    (fn [[col row]]
      (for [n (next (range))
            :let [x (+ col n) y (+ row n)]
            :while (and (< x cols)  (< y rows))
            :when (seats [x y])]
        [x y]))
    ;down
    (fn [[col row]]
      (for [x (range (inc row) rows)
            :when (seats [col x])]
        [col x]))
    ;diag down left
    (fn [[col row]]
      (for [n (next (range))
            :let [x (- col n) y (+ row n)]
            :while (and (>= x 0)  (< y rows))
            :when (seats [x y])]
        [x y]))
    ;left
    (fn [[col row]]
      (for [x (range (dec col) -1 -1)
            :when (seats [x row])]
        [x row]))
    ;diag up left
    (fn [[col row]]
      (for [n (next (range))
            :let [x (- col n) y (- row n)]
            :while (and (>= x 0)  (>= y 0))
            :when (seats [x y])]
        [x y]))])

(defn count-occupied-by-sight [seat occupied directions]
  (let [sights (map #(% seat) directions)]
    (count
      (filter
        identity
        (for [sight sights]
          (occupied (first sight)))))))


(defn will-be-occupied-sight? [seat occupied directions]
  (let [is-occupied (occupied seat)
        adjacent-count (count-occupied-by-sight seat occupied directions)]
    ;(println "adjacent " adjacent-count " is-occupied" is-occupied)
    (if (and (not is-occupied ) (zero? adjacent-count))
      true
      (if (and is-occupied (<= 5 adjacent-count))
        false
        is-occupied))))

(defn step-sight [seats occupied directions]
  (set (filter #(will-be-occupied-sight? % occupied directions) seats)))

(defn run-til-stable-sight [seats directions]
  (loop [occupied #{}]
    (let [to-be-occupied (step-sight seats occupied directions)]
      (if (= occupied to-be-occupied)
        occupied
        (recur to-be-occupied)))))

(defn ex2 [opts]
  (let [lines (read-input)
        cols (count (first lines))
        rows (count lines)
        seats (parse-seats lines)
        directions (lines-of-sight [cols rows] seats)]
    (println (count (run-til-stable-sight seats directions)))))

(defn test-dirs [opts]
  (println (map #(% [5 5]) (lines-of-sight [10 10] any?))))
