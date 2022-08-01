package com.dxc.CUBIC.entities;

import java.util.ArrayList;

public class ResponseDetails {
    private ArrayList<Employee> employeesRollingOff;
    private ArrayList<Employee> employeesNonWholeAllocation;

    public ResponseDetails() {
        employeesRollingOff = new ArrayList<Employee>();
        employeesNonWholeAllocation = new ArrayList<Employee>();
    }

    public ArrayList<Employee> getEmployeesRollingOff() {
        return employeesRollingOff;
    }

    public void setEmployeesRollingOff(ArrayList<Employee> employeesRollingOff) {
        this.employeesRollingOff = employeesRollingOff;
    }

    public ArrayList<Employee> getEmployeesNonWholeAllocation() {
        return employeesNonWholeAllocation;
    }

    public void setEmployeesNonWholeAllocation(ArrayList<Employee> employeesNonWholeAllocation) {
        this.employeesNonWholeAllocation = employeesNonWholeAllocation;
    }

}
