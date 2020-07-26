var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],            /* FlaskとVueのデリミタが一緒なので共存させるためにVueのデリミタを [[ hoge ]] に変更する */
    data:{
        message:'Hello Vue.js!'
    }
})
