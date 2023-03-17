     function search() {
       var query = document.getElementById('query').value;
       var xhr = new XMLHttpRequest();
       var resultList = document.getElementById('results')
       url='spotify/search?query=' + query;
       xhr.open('GET', url, true);
       xhr.onreadystatechange = function() {
         if (xhr.readyState === xhr.DONE && xhr.status === 200) {
           var results = JSON.parse(xhr.responseText);
           newListHTML = results.data.map(item => `<li>${item}</li>`)
           if (results.success) {
                resultList.innerHTML = newListHTML.join('');
           }
           else{
                resultList.innerHTML = 'Processing failed';
           }

         }
       };
       xhr.send();
     }
