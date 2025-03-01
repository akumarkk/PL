package com.example.svcapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
@RestController
public class DemoApplication {
	static Hello hello;

	public static void main(String[] args) {
		ApplicationContext context =SpringApplication.run(DemoApplication.class, args);
		 
		hello = context.getBean(Hello.class);
		//  hello.show();
	}

	private List<String> data = new ArrayList<>();
	@GetMapping("/get")
    public List<String> getData() {
        return data;
    }

	@GetMapping("/adddata")
    public String postSampleData() {
        // data.add("Yash");
		// data.add("Punith");
		// data.add("Suraj");
        return DemoApplication.hello.show(data);
    }

}
