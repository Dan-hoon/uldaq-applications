package com.dxc.CUBIC;

import java.sql.*;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.dxc.CUBIC.entities.RequestDetails;
import com.dxc.CUBIC.entities.ResponseDetails;
import com.dxc.CUBIC.util.QueryHelper;

public class App implements RequestHandler<RequestDetails, ResponseDetails> {

    @Override
    // entry point for the lambda function
    // requestDetails is the POJO representation of the query parameters
    public ResponseDetails handleRequest(RequestDetails requestDetails, Context context) {

        // initialize the list of employees to return through the API
        ResponseDetails response = new ResponseDetails();

        try {

            QueryHelper helpMe = new QueryHelper();
            // Populate the list of employees
            helpMe.requestToEmployeeList(requestDetails, response);

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        // Return the list of employees
        return response;
    }
}
