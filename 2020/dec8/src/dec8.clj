(ns dec8
  (:require [clojure.string :as str :refer [split]]))

(defn read-input []
  (line-seq (java.io.BufferedReader. *in*)))

(defn parse-inst [ins-str]
  (let [[inst op] (str/split ins-str #" ")]
    [inst (Integer/parseInt op)]))

(defn load-prg [lines]
  (vec (map parse-inst lines)))

(defn init-prg-state [prg]
  {
   :acc 0
   :pos 0
   :prg prg
   :visited #{}})

(defn step [state]
  (let [[inst op] (get (:prg state) (:pos state))]
    (condp = inst
      "nop" {:acc (:acc state) :pos (inc (:pos state)) :prg (:prg state) :visited (conj (:visited state) (:pos state))}
      "acc" {:acc (+ (:acc state) op) :pos (inc (:pos state)) :prg (:prg state) :visited (conj (:visited state) (:pos state))}
      "jmp" {:acc (:acc state) :pos (+ (:pos state) op) :prg (:prg state) :visited (conj (:visited state) (:pos state))}
      (println inst op))))

(defn get-final-state [prg]
  (loop [s (init-prg-state prg)]
      (if (or (contains? (:visited s) (:pos s)) (>= (:pos s) (count (:prg s))))
        s
        (recur (step s)))))

(defn prg-terminates [prg]
  (<= (count prg) (:pos (get-final-state prg))))

(defn swap-inst [[inst op]]
  (cond
    (= inst "jmp") ["nop" op]
    (= inst "nop") ["jmp" op]
    :else [inst op]))

(defn swap-inst-at [prg pos]
  (assoc prg pos (swap-inst (get prg pos))))

(defn ex1 [opts]
  (println (:acc (get-final-state (load-prg (read-input))))))

(defn ex2 [opts]
  (let [prg (load-prg (read-input))]
    (println (:acc (get-final-state (first (filter prg-terminates (map #(swap-inst-at prg %) (range (count prg))))))))))
