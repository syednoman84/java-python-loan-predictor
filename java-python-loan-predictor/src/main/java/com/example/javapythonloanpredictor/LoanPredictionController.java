package com.example.javapythonloanpredictor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/loan")
public class LoanPredictionController {

    @Autowired
    private LoanPredictionService predictionService;

    @PostMapping("/predict")
    public ResponseEntity<LoanPredictionResponse> predict(@RequestBody LoanPredictionRequest request) {
        return ResponseEntity.ok(predictionService.predictDefault(request));
    }

    @PostMapping("/predict/lc")
    public ResponseEntity<LoanPredictionResponse> predict_lc(@RequestBody LoanPredictionRequestLC request) {
        return ResponseEntity.ok(predictionService.predictDefaultLC(request));
    }
}
