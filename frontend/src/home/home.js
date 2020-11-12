import React from 'react';
import { Link } from 'react-router-dom';
import TopBar from '../topbar/topbar';

function Home(){
    return (
        <div>
            <TopBar title="Home"/>
            <nav>
                <p>
                    <Link to="/">Home</Link>
                </p>
                <p>
                    <Link to="/mnist">MNIST</Link>
                </p>
                <p>
                    <Link to="/gpt2">GPT2</Link>
                </p>
            </nav>
        </div>
    )
}
export default Home;