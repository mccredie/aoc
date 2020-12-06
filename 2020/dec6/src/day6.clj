(ns day6
  (:require [clojure.set :as cset :refer [intersection]]))

(declare read-input)

(def questions (set "abcdefghijklmnopqrstuvwxyz"))

(defn get-groups-any [lines]
  (let [[groups lastgroup]
        (reduce
          (fn
            [[groups current] row]
            (if (empty? row)
              [(conj groups current) #{}]
              [groups (reduce conj current row)]))
          [[] #{}]
          lines)]
    (conj groups lastgroup)))

(defn ex1 [opts]
  (println (reduce + (map count (get-groups-any (read-input))))))

(defn get-groups-all [lines]
  (let [[groups lastgroup]
        (reduce
          (fn
            [[groups current] row]
            (if (empty? row)
              [(conj groups current) questions]
              [groups (cset/intersection current (set row))]))
          [[] questions]
          lines)]
    (conj groups lastgroup)))

(defn ex2 [opts]
  (println (reduce + (map count (get-groups-all (read-input))))))

(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

