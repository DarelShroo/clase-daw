let products = [
  {
    id: 0,
    name: 'Product 1',
    price: 100,
    img: 'images/product0.png',
  },
  {
    id: 1,
    name: 'Product 2',
    price: 200,
    img: 'images/product1.png',
  },
  {
    id: 2,
    name: 'Product 3',
    price: 300,
    img: 'images/product2.png',
  },
];

let body = document.getElementById('body');

products.forEach((item) => {
  body.innerHTML += `
    <div>
      <h1>Product Name: ${item.name}</h1>
      <span>Price: ${item.price}</span>
      <img src="${item.img}" alt="${item.id}">
    </div>
  `;
});
