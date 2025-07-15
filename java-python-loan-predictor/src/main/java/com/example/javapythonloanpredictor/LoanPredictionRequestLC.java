package com.example.javapythonloanpredictor;

import com.fasterxml.jackson.annotation.JsonProperty;

public class LoanPredictionRequestLC {

    @JsonProperty("loan_amnt")
    private double loanAmnt;

    @JsonProperty("term")
    private double term;

    @JsonProperty("int_rate")
    private double intRate;

    @JsonProperty("annual_inc")
    private double annualInc;

    @JsonProperty("emp_length")
    private double empLength;

    @JsonProperty("dti")
    private double dti;

    @JsonProperty("fico_range_high")
    private double ficoRangeHigh;

    // Getters & Setters for all
    public double getLoanAmnt() { return loanAmnt; }
    public void setLoanAmnt(double loanAmnt) { this.loanAmnt = loanAmnt; }

    public double getTerm() { return term; }
    public void setTerm(double term) { this.term = term; }

    public double getIntRate() { return intRate; }
    public void setIntRate(double intRate) { this.intRate = intRate; }

    public double getAnnualInc() { return annualInc; }
    public void setAnnualInc(double annualInc) { this.annualInc = annualInc; }

    public double getEmpLength() { return empLength; }
    public void setEmpLength(double empLength) { this.empLength = empLength; }

    public double getDti() { return dti; }
    public void setDti(double dti) { this.dti = dti; }

    public double getFicoRangeHigh() { return ficoRangeHigh; }
    public void setFicoRangeHigh(double ficoRangeHigh) { this.ficoRangeHigh = ficoRangeHigh; }
}
