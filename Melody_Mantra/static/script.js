     function search() {
       var query = document.getElementById('query').value;
       var xhr = new XMLHttpRequest();
       var resultList = document.getElementById('results')
       url='spotify/search?query=' + query;
       xhr.open('GET', url, true);
       xhr.onreadystatechange = function() {
         if (xhr.readyState === xhr.DONE && xhr.status === 200) {
           var results = JSON.parse(xhr.responseText);
           var itemList = results;
           var newListHTML = "<ul>";
           for (var i = 0; i < itemList.length; i++) {
                newListHTML += "<li>" + itemList[i] + "</li>";
           }
           newListHTML += "</ul>";
           resultList.innerHTML = newListHTML;
         }
       };
       xhr.send();
     }
