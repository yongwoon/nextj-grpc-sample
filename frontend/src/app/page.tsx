"use client";

import { useEffect, useState } from "react";
import { grpc } from "@improbable-eng/grpc-web";
import { HelloRequest, HelloReply } from "../proto/helloworld_pb";
import { GreeterClient } from "../proto/HelloworldServiceClientPb";

const Home: React.FC = () => {
  const [message, setMessage] = useState<string>("");

  useEffect(() => {
    const client = new GreeterClient("http://localhost:8080");

    const request = new HelloRequest();
    request.setName("World");

    client.sayHello(request, {}, (err, response: HelloReply) => {
      if (err) {
        console.error(err);
        return;
      }
      setMessage(response.getMessage());
    });
  }, []);

  return (
    <div>
      <h1>gRPC-Web with Next.js App Router</h1>
      <p>{message}</p>
    </div>
  );
};

export default Home;
