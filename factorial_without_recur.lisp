;factorial of a number without recursion

(defun factorial (n)
	(setf fact 1)  	
	(loop for i from 1 to n
      		do(setf fact (* fact i))
     	)
	fact
)
(write-line "Enter a number : ")
(setf num (read))
(format t "Factorial of ~d is: ~d" num (factorial num))
