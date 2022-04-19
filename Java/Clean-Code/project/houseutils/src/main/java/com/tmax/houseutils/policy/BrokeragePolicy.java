package com.tmax.houseutils.policy;


import com.tmax.houseutils.exception.ErrorCode;
import com.tmax.houseutils.exception.HouseUtilsException;

import java.util.List;

/**
 * @author Happy
 *
*/
public interface BrokeragePolicy {

    List<BrokerageRule> getRules();

    default Long calculate(Long price) {
        BrokerageRule brokerageRule = getRules().stream()
                .filter(rule -> price < rule.getLessThan())
                .findFirst().orElseThrow(() -> new HouseUtilsException(ErrorCode.INTERNAL_ERROR));
        return brokerageRule.calcMaxBrokerage(price);
    }
}
