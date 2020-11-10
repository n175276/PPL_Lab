;factorial of a number with recursion

(defun factorial (n)
	(cond 
		((zerop n) 1)
    		(t ( * n (factorial (- n 1))))
   	)
)
(write-line "Enter a number : ")
(setf num (read))
(format t "Factorial of ~d is: ~d" num (factorial num))




