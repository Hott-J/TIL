package com.tmax.houseutils.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HealthChecktController {

    @GetMapping("/api/ping")
    public String ping() {
        return "ok";
    }
}
