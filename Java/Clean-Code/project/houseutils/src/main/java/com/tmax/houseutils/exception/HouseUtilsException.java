package com.tmax.houseutils.exception;

/**
 * @author Happy
 */
public class HouseUtilsException extends RuntimeException {
    private ErrorCode errorCode;
    private String message;

    public HouseUtilsException(ErrorCode errorCode) {
        this(errorCode, errorCode.getMessage());
    }

    public HouseUtilsException(ErrorCode errorCode, String customMessage) {
        super(customMessage); // RuntimeException의 message를 상속
        this.errorCode = errorCode;
        this.message = customMessage;
    }
}
