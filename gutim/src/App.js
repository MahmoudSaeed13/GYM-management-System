import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import './App.css';
import Header from './components/header';
import Footer from './components/footer';
import Home from './components/home';
import About from './components/about';
import Classes from './components/classes';
import Gallery from './components/gallery';
import Contact from './components/contact';
import Login from './components/login';
import Signup from './components/signup';
// import Products from './components/products';
// import ProductDetails from './components/productDetails';
// import Cart from './components/cart';
// import Checkout from './components/checkout';
// import Confirmation from './components/confirmation';

function App() {
  return (
    <React.Fragment>
      <Header />
      <Routes>
        <Route path="/" element={<Navigate to={'home'} />} />
        <Route path="home" element={<Home />} />
        <Route path="classes" element={<Classes />} />
        <Route path="gallery" element={<Gallery />} />
        <Route path="about" element={<About />} />
        <Route path="contact" element={<Contact />} />
        <Route path="login" element={<Login />} />
        <Route path="signup" element={<Signup />} />
        {/* <Route path="products" element={<Products />} />
        <Route path="products/:id" element={<ProductDetails />} />
        <Route path="cart" element={<Cart />} />
        <Route path="checkout" element={<Checkout />} />
        <Route path="confirmation" element={<Confirmation />} /> */}
      </Routes>
      <Footer />
    </React.Fragment>
  );
}

export default App;
