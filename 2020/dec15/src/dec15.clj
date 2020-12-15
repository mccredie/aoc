(ns dec15
  (:require [clojure.string :as str :refer [split]]))

(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

(defn parse-input [line]
  (map #(Integer/parseInt %) (str/split line #",")))

(defn next-game-seq [last-seen index value]
  (cons value (lazy-seq (next-game-seq
                          (assoc last-seen value index)
                          (inc index)
                          (- index (get last-seen value index))))))

(defn game-seq [start-seq]
  (let [last-seen (into {} (map vector (butlast start-seq) (range)))]
    (concat
      (butlast start-seq)
      (next-game-seq
        last-seen
        (dec (count start-seq))
        (last start-seq)))))


(defn ex1 [opts]
  (println (nth (game-seq (parse-input (first (read-input)))) 2019)))

(defn ex2 [opts]
  (println (nth (game-seq (parse-input (first (read-input)))) 29999999)))
