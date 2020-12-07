(ns dec7
  (:require [clojure.string :as str :refer [split]]))

(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

(def rule-regex #"(?<bag>[a-z]+ [a-z]+) bags contain (?<contents>.*)\.")
(def contents-rule #"(?<count>\d+) (?<bag>[a-z]+ [a-z]+) bags?")

(defn match-bag [line] (re-matcher rule-regex line))
(defn match-contents [contents-str] (re-matcher contents-rule contents-str))

(defn to-contents [matcher]
  (if
    (.matches matcher)
    { (.group matcher "bag") (Integer/parseInt (.group matcher "count")) }))

(defn parse-contents [contents-str]
  (if
    (= "no other bags" contents-str)
    {}
    (apply merge (map
      (fn [contents]
        (to-contents (match-contents contents)))
      (str/split contents-str #", ")))))

(defn to-bag-rule [matcher]
  (if
    (.matches matcher)
    { (.group matcher "bag") (parse-contents (.group matcher "contents"))}))

(defn parse-bag [line] (->>
                        line
                        match-bag
                        to-bag-rule))

(defn read-rules [] (apply merge (map parse-bag (read-input))))

(defn bags-containing [rules color found-already]
 (reduce
   (fn [bags [bag contents]]
     (if
       (and
         (not (contains? found-already bag))
         (contains? contents color))
       (bags-containing rules bag (conj bags bag))
       bags))
     found-already
     rules))

(declare bags-count)

(defn bags-count-raw [rules outer-bag]
  (reduce + (map
              (fn [[bag cnt]] (+ cnt (* cnt (bags-count rules bag))))
              (get rules outer-bag))))

(def bags-count (memoize bags-count-raw))

(defn ex1 [opts]
     (println (count (bags-containing (read-rules) "shiny gold" #{}))))

(defn ex2 [opts]
    (println (bags-count (read-rules) "shiny gold")))

