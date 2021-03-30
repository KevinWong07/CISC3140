;This file is for currency conversions
;between the US Dollar and the Chinese Yuan

;Please note: all converted values are current
;as of 2021/03/30 at 10AMEST. Change values if different day

;self-explanatory, just converts dollar to yuan
(define usd-to-cny 
  (lambda (n)
    (* n 6.57)
  )
)

;converts yuan to dollar
(define cny-to-usd
  (lambda (n)
    (* n 0.15)
  )
)