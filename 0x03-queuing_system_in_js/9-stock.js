#!/usr/bin/node
import express from "express";
import redis from "redis";
import { promisify } from "util";

const listProducts = [
  {
    id: 1,
    name: "Suitcase 250",
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: "Suitcase 450",
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: "Suitcase 650",
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: "Suitcase 1050",
    price: 550,
    stock: 5
  }
];

const server = express();

const client = redis.createClient();

// promisify redis client
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const getItemById = id => {
  return listProducts.find(product => product.id === id);
};

const reserveStockById = (itemId, stock) => {
  client.set("item." + itemId, stock);
};

const getCurrentReservedStockById = async itemId => {
  const stock = await getAsync("item." + itemId);
  return stock !== null ? parseInt(stock) : 0;
};

server.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);

  const item = getItemById(itemId);
  if (!item) return res.status(404).json({ status: "Product not found" });

  const currentStock =
    (await getCurrentReservedStockById(itemId)) || item.stock;
  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: currentStock
  });
});

server.get("/list_products", (req, res) => {
  const formattedProducts = listProducts.map(product => {
    return {
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock
    };
  });
  res.json(formattedProducts);
});

server.listen(1245);
