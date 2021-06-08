import express from "express";
import mysql from "mysql";
import cors from "cors";
import https from "https";

import "dotenv/config";

/* database 연동 */

const app = express();
app.set("port", process.env.PORT || 3000);

app.get("/", (req, res) => {
  res.send("Hello, express");
});

app.listen(app.get("port"), () => {
  console.log(app.get("port"), "번 포트에서 실행");
});

const connection = mysql.createConnection({
  host: "localhost",
  user: process.env.LOCAL_DATABASE_USERNAME,
  password: process.env.LOCAL_DATABASE_PASSWORD,
  database: process.env.LOCAL_DATABASE_NAME,
});

connection.connect();
