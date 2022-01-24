 var updateBtns = document.getElementsByClassName('update-cart')

 for (var i = 0; i < updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function () {
         var contentId = this.dataset.content
         var action = this.dataset.action
         console.log('contentId:', contentId, 'action:', action)

         if (user === 'AnonymousUser'){
             console.log('not logged in')
         }else {
             updateUserOrder(contentId, action)
         }
     })
 }


function updateUserOrder(contentId, action) {
    console.log('user is logged in sending data...')


    var url = '/basket/add_to_basket/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'contentId': contentId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
    })

}
