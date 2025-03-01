package com.example.svcapp;
import org.springframework.stereotype.Component;
import java.util.ArrayList;
import java.util.List;

@Component
public class Hello {
    public String show(List<String> data) {

        System.out.println("Hello, world!");
        // data = new ArrayList<>();
        data.add("Yash");
        data.add("Yash");
		data.add("Punith");
		data.add("Suraj");
        return "Data added: " + data;
    }

}
