package com.tmax.houseutils.policy;

import lombok.Getter;

import java.util.Arrays;
import java.util.List;

/**
 * @author Happy
 * <p>
 * 임대차일 때 중개수수료를 계산해주는 클래스
 */
@Getter
public class RentBrokeragePolicy implements BrokeragePolicy{
    public Long calculate(Long price) {
        BrokerageRule rule = createBrokerageRule(price);
        return rule.calcMaxBrokerage(price);
    }

    public BrokerageRule createBrokerageRule(Long price) {
        BrokerageRule rule;
        if (price < 50_000_000) {
            rule = new BrokerageRule(0.5, 200_000L);
        } else if (price < 200_000_000) {
            rule = new BrokerageRule(0.4, 300_000L);
        } else if (price < 600_000_000) {
            rule = new BrokerageRule(0.3, null);
        } else if (price < 900_000_000) {
            rule = new BrokerageRule(0.4, null);
        } else {
            rule = new BrokerageRule(0.8, null);
        }
        return rule;
    }
}
