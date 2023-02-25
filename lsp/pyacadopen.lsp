(defun pyacadopen (dwg)
    (vl-load-com)
    (vla-open (vla-get-documents (vlax-get-acad-object)) 
              dwg
    )
	(princ)
)