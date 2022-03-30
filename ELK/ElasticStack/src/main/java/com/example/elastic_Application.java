package com.example;

import org.elasticsearch.action.admin.indices.create.CreateIndexRequest;
import org.elasticsearch.common.settings.Settings;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class elastic_Application {
    public static void main(String[] args) {
        SpringApplication.run(elastic_Application.class, args);
    }
}