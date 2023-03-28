import React, { useState } from 'react';
import axios from 'axios';

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [result, setResult] = useState([]);
  const [page, setPage] = useState(1);
  // const [nextClicked, setNextClicked] = useState(false);

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/movie/search?query=${query}`);
      let something = response['data']['data'];
      setResults(something);
      console.log(something);
      setPage(2);
      // setNextClicked(false); // Reset the nextClicked state
    } catch (error) {
      setResults("no resulsts found");
      console.log(results);
    }
  };

  const handleNext = async () => {
    try {
      const nextPage = page + 1;
      const response = await axios.get(`http://localhost:5000/movie/search?query=${query}&page=${page}`);
      let some = response['data']['data'];
      if (some.length > 0) {
        setResult(some);
        setPage(nextPage);
        setResults([]);
        // setNextClicked(true); // Set the nextClicked state to true
      } else {
        setPage(page);
        setResults([]);
        console.log(some);
      }
    } catch (error) {
      setResult("no resulsts found");
      console.log(results);
    }
  };

  return (
    <div>
      <input type="text" value={query} onChange={handleInputChange} />
      {/* {!nextClicked && <button onClick={handleSearch}>Search</button>} */}
      <button onClick={handleSearch}>Search</button>
      <button onClick={handleNext}>Next results</button>
      {Array.isArray(results) ? (
        <ul>
          {results.map((value) => (
            <li key={value.id}>
              {value.id} =={" "}
              <img
                src={value.image}
                style={{ width: "50%", height: "400px" }}
              />
            </li>
          ))}
        </ul>
      ) : (
        <p>No results found</p>
      )}
      {Array.isArray(result) ? (
        <ul>
          {result.map((value) => (
            <li key={value.id}>
              {value.id} =={" "}
              <img
                src={value.image}
                style={{ width: "50%", height: "400px" }}
              />
            </li>
          ))}
        </ul>
      ) : (
        <p>No results found</p>
      )}
    </div>
  );
}

export default Search;
