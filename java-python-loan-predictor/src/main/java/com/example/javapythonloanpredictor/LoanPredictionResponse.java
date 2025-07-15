package com.example.javapythonloanpredictor;

import com.fasterxml.jackson.annotation.JsonProperty;

public class LoanPredictionResponse {
    @JsonProperty("default_risk")
    private int defaultRisk;

    public int getDefaultRisk() {
        return defaultRisk;
    }

    public void setDefaultRisk(int defaultRisk) {
        this.defaultRisk = defaultRisk;
    }
}
