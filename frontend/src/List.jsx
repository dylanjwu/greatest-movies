import React from 'react';

class List extends React.Component {
    constructor(){
        super();
        this.state = {
            movies: null
        }
    }

    async componentDidMount(){
        const response = await fetch('http://localhost:3000');
        const collection = await response.json();
        this.setState({movies:this.renderMovies(collection)}, ()=> console.log(this.state.movies));
    }

    renderMovies(collection){
        return Object.keys(collection).map((k)=>
            <li className="listing" key={k}><span className="title">{k}  </span>
                        <span className="year">({collection[k]['year']})</span>
            </li>);
    }

    render(){
        return (
            <div className="list-container">
                <ol className="movie-list">{this.state.movies}</ol>
            </div>
        )
    }
}

export default List;