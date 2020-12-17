(ns dec17
  (:require [clojure.set :as cset :refer [intersection]]) )

(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

(defn parse-conway [lines dims]
  (set (for [[y line] (map vector (range) lines)
       [x c]  (map vector (range) line) :when (= c \#)]
    (concat [x y] (take (- dims 2) (repeat 0))))))

(defn cart [colls]
  (if (empty? colls)
    '(())
    (for [more (cart (rest colls))
          x (first colls)]
      (cons x more))))

(defn adjacent [cell]
    (map
      (fn [a b] (vec (map + a b)))
      (repeat cell)
      (cart (take (count cell) (repeat [-1 0 1])))))

(defn cells-to-consider [alive]
  (into #{} (apply concat (map adjacent alive))))

(defn active-adjacent [alive cell]
  (count (cset/intersection (disj alive cell) (set (adjacent cell)))))

(defn will-live [is-alive live-neighbors]
  (or
    (and is-alive (#{2 3} live-neighbors))
    (and (not is-alive) (= 3 live-neighbors))))


(defn step [alive]
  (set
    (filter
      #(will-live (alive %) (active-adjacent alive %))
      (cells-to-consider alive))))

(defn run [alive]
  (iterate step alive))

(defn ex1 [opts]
  (println (count (nth (run (parse-conway (read-input) 3)) 6))))

(defn ex2 [opts]
  (println (count (nth (run (parse-conway (read-input) 4)) 6))))

