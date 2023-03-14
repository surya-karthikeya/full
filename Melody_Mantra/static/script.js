     function search() {
       var query = document.getElementById('query').value;
       var xhr = new XMLHttpRequest();
       var resultList = document.getElementById('results')
       url='spotify/search?query=' + encodeURIComponent(query);
       xhr.open('GET', url, true);
       xhr.onreadystatechange = function() {
         if (xhr.readyState === xhr.DONE && xhr.status === 200) {
           var results = JSON.parse(xhr.responseText);
           resultList.innerHTML = xhr.responseText;
         }
       };
       xhr.send();
     }
