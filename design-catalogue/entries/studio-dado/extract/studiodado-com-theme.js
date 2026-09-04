// React Theme — extracted from https://www.studiodado.com/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '187.733': string;
    '138.24': string;
    '59.7333': string;
    '34.1333': string;
    '25.6': string;
    '17.0667': string;
    '11.9467': string;
    '8.53333': string;
 *   };
 *   space: {
    '9': string;
    '85': string;
    '120': string;
    '154': string;
    '208': string;
    '239': string;
    '282': string;
    '316': string;
    '394': string;
    '444': string;
 *   };
 *   radii: {
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "background": "#5d5346",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#1b1b1c",
    "neutral300": "#5d5346"
  },
  "fonts": {
    "body": "'disp', sans-serif"
  },
  "fontSizes": {
    "187.733": "187.733px",
    "138.24": "138.24px",
    "59.7333": "59.7333px",
    "34.1333": "34.1333px",
    "25.6": "25.6px",
    "17.0667": "17.0667px",
    "11.9467": "11.9467px",
    "8.53333": "8.53333px"
  },
  "space": {
    "9": "9px",
    "85": "85px",
    "120": "120px",
    "154": "154px",
    "208": "208px",
    "239": "239px",
    "282": "282px",
    "316": "316px",
    "394": "394px",
    "444": "444px"
  },
  "radii": {
    "full": "9999px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "background": {
      "default": "#5d5346",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "34.1333px",
      "fontWeight": "400",
      "lineHeight": "40.96px"
    },
    "h2": {
      "fontSize": "25.6px",
      "fontWeight": "400",
      "lineHeight": "28.16px"
    },
    "body1": {
      "fontSize": "17.0667px",
      "fontWeight": "400",
      "lineHeight": "20.48px"
    }
  },
  "shape": {
    "borderRadius": 9999
  },
  "shadows": []
};

export default theme;
