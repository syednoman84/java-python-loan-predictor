package com.example.javapythonloanpredictor;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class LoanPredictionService {

    private final RestTemplate restTemplate = new RestTemplate();

    public LoanPredictionResponse predictDefault(LoanPredictionRequest request) {
        String url = "http://localhost:8000/predict";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<LoanPredictionRequest> entity = new HttpEntity<>(request, headers);

        return restTemplate.postForObject(url, entity, LoanPredictionResponse.class); // ✅ Return full object
    }

    public LoanPredictionResponse predictDefaultLC(LoanPredictionRequestLC request) {
        String url = "http://localhost:8000/predict/lc";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<LoanPredictionRequestLC> entity = new HttpEntity<>(request, headers);

        return restTemplate.postForObject(url, entity, LoanPredictionResponse.class);
    }


}
