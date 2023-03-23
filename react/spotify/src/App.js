import React, { useState } from 'react';
import axios from 'axios';


function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSearch = async () => {
  const response = await axios.get(`http://localhost:5000/spotify/search?query=${query}`);
  let something = response['data']['data'];
  setResults(something);
  // console.log(something);
  };


  return (
    <div>
      <input type="text" value={query} onChange={handleInputChange} />
      <button onClick={handleSearch}>Search</button>

      <ul>
      {results.map((value) => (
          <li key={value}>
            {value.artist} == <img src={value.image} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Search;
