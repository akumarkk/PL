package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
@RestController
public class MyprojectApplication {

	public static void main(String[] args) {
		SpringApplication.run(MyprojectApplication.class, args);
	}


	List<String> data = new ArrayList<>();
	@GetMapping("/get")
    public List<String> getData() {
        return data;
    }

	@GetMapping("/adddata")
    public String postSampleData() {
        data.add("Yash");
		data.add("Punith");
		data.add("Suraj");
        return "Data added: " + data;
    }

    @PostMapping("/post")
    public String postData(@RequestBody String newData) {
        data.add(newData);
        return "Data added: " + newData;
    }

    @GetMapping("/get/{index}")
    public String getDataByIndex(@PathVariable int index) {
        if (index >= 0 && index < data.size()) {
            return data.get(index);
        } else {
            return "Index out of bounds";
        }
    }

    @DeleteMapping("/delete/{index}")
    public String deleteDataByIndex(@PathVariable int index){
        if(index >=0 && index < data.size()){
            String removed = data.remove(index);
            return "removed: " + removed;
        } else {
            return "index out of bounds";
        }
    }

}
