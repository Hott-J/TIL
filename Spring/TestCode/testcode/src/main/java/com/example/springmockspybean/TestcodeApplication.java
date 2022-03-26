package com.example.springmockspybean;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class TestcodeApplication {

	@Bean
	public ObjectMapper objectMapper () {
		return new ObjectMapper();
	}

	public static void main(String[] args) {
		SpringApplication.run(TestcodeApplication.class, args);
	}

}
