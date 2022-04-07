package com.tmax.houseutils.policy;


import com.tmax.houseutils.exception.ErrorCode;
import com.tmax.houseutils.exception.HouseUtilsException;

import java.util.List;

/**
 * @author Happy
 *
*/
public interface BrokeragePolicy {

    BrokerageRule createBrokerageRule(Long price);

    default Long calculate(Long price) {
        BrokerageRule rule = createBrokerageRule(price);
        return rule.calcMaxBrokerage(price);
    }
}
