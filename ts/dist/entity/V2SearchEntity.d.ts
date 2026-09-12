import { FreeMusicEntityBase } from '../FreeMusicEntityBase';
import type { FreeMusicSDK } from '../FreeMusicSDK';
import type { Control } from '../types';
import type { V2Search, V2SearchLoadMatch } from '../FreeMusicTypes';
declare class V2SearchEntity extends FreeMusicEntityBase<V2Search> {
    constructor(client: FreeMusicSDK, entopts: any);
    make(this: V2SearchEntity): V2SearchEntity;
    load(this: any, reqmatch?: V2SearchLoadMatch, ctrl?: Control): Promise<V2SearchEntity>;
}
export { V2SearchEntity };
