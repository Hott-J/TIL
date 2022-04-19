package com.tmax.houseutils.policy;

import lombok.Getter;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author Happy
 * <p>
 * 매매일 때 중개수수료를 계산해주는 클래스
 */
@Getter
public class PurchaseBrokeragePolicy implements BrokeragePolicy{

    private final List<BrokerageRule> rules;

    public PurchaseBrokeragePolicy() {
        rules = Arrays.asList(
                new BrokerageRule(50_000_000L,0.6, 250_000L),
                new BrokerageRule(50_000_000L,0.6, 250_000L),
                new BrokerageRule(60_000_000L,0.4),
                new BrokerageRule(90_000_000L,0.5),
                new BrokerageRule(Long.MAX_VALUE,0.9)
        );
    }
}
