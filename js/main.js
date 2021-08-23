console.log('PregunChaco')

$.ajax({
    type: 'GET',
    url: '/api/empezar-trivia/',
    success: function(response) {
        console.log(response)
    },
    error: function(error) {
        console.log('error', error)
    }
})