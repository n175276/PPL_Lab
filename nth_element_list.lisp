;getting nth element from a list

(write-line "Enter list : ")
(setf l (read-from-string (concatenate 'string "(" (read-line) ")")))
(write-line "Enter index : ")
(setf index (read))
(setf res (nth index l))
(format t "Element at position ~d : ~d" index res)
