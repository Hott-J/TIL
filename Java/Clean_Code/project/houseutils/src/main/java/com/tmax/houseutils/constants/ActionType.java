package com.tmax.houseutils.constants;

import lombok.AllArgsConstructor;

/**
 * @author Happy
 */
@AllArgsConstructor
public enum ActionType {
    PURCHASE("매매"),
    RENT("임대차");

    private String description;
}
