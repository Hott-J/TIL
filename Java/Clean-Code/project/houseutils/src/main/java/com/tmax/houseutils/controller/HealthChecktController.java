package com.tmax.houseutils.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 *
 * 서비스 헬스 체크를 위한 컨트롤러러 */
@RestController
public class HealthChecktController {

    @GetMapping("/api/ping")
    public String ping() {
        return "ok";
    }
}
