(ns dec17
  (:require [clojure.set :as cset :refer [intersection]]) )

(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

(defn parse-conway [lines & {:keys [dims] :or {dims 2}}]
  (set
    (for [[y line] (map vector (range) lines)
          [x c]  (map vector (range) line)
          :when (= c \#)]
      (concat [x y] (take (- dims 2) (repeat 0))))))

(defn cart
  "cartesian product of collections"
  [colls]
  (if (empty? colls)
    '(())
    (for [more (cart (rest colls))
          x (first colls)]
      (cons x more))))

(defn adjacent [cell]
  (for [offset (cart (take (count cell) (repeat [-1 0 1])))
        :when (not-every? zero? offset)]
    (vec (map + offset cell))))

(defn cells-to-consider [alive]
  (mapcat adjacent alive))

(defn alive-adjacent [alive cell]
  (count (cset/intersection alive (set (adjacent cell)))))

(defn will-live [is-alive live-neighbors]
  (or
    (and is-alive (#{2 3} live-neighbors))
    (and (not is-alive) (= 3 live-neighbors))))

(defn step [alive]
  (set
    (filter
      #(will-live (alive %) (alive-adjacent alive %))
      (cells-to-consider alive))))

(defn run [alive]
  (iterate step alive))

(defn ex1 [opts]
  (println (count (nth (run (parse-conway (read-input) :dims 3)) 6))))

(defn ex2 [opts]
  (println (count (nth (run (parse-conway (read-input) :dims 4)) 6))))
