     function search() {
       var query = document.getElementById('query').value;
       var xhr = new XMLHttpRequest();
       var resultList = document.getElementById('results')
       url='spotify/search?query=' + query;
       xhr.open('GET', url, true);
       xhr.onreadystatechange = function() {
         if (xhr.readyState === xhr.DONE && xhr.status === 200) {
         var results = JSON.parse(xhr.responseText);
           if (results.success) {
<<<<<<< HEAD
                newListHTML = results.data.map(item => `<li>${item}</li>`)
=======
                newListHTML = results.data.map((item, image) => `<li>${item} ==>> <img src=${results.image[image]}></li>`);
>>>>>>> Experimental
                resultList.innerHTML = newListHTML.join('');
           }
           else{
                resultList.innerHTML = 'Processing failed';
           }
         }
       };
       xhr.send();
     }
