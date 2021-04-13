## Kevin Wong
## CISC 3140
## Lab 8

Learn, understand, and write code using Javascript.
All files can be found under /Lab 8/

```javascript
// grabs input from 'phone' element and runs it through function (e)
document.getElementById('phone').addEventListener('input', function (e) {
    // declares a variable 'x' and checks if input is a number
    // if input is not number, it won't show up
    var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
    // checks inputs and if matches the above, it appends a '-' after each number group 
    e.target.value = !x[2] ? x[1] : x[1] + '-' + x[2] + (x[3] ? '-' + x[3] : '');
});
```
