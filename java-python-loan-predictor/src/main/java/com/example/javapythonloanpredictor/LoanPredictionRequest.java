package com.example.javapythonloanpredictor;

import com.fasterxml.jackson.annotation.JsonProperty;

public class LoanPredictionRequest {
    @JsonProperty("income")
    private double income;

    @JsonProperty("loan_amount")
    private double loanAmount;

    @JsonProperty("term")
    private int term;

    @JsonProperty("credit_score")
    private double creditScore;

    // Getters and Setters
    public double getIncome() { return income; }
    public void setIncome(double income) { this.income = income; }

    public double getLoanAmount() { return loanAmount; }
    public void setLoanAmount(double loanAmount) { this.loanAmount = loanAmount; }

    public int getTerm() { return term; }
    public void setTerm(int term) { this.term = term; }

    public double getCreditScore() { return creditScore; }
    public void setCreditScore(double creditScore) { this.creditScore = creditScore; }
}
